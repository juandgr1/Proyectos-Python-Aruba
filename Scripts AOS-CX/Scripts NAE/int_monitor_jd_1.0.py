#Copyright (c) 2017 Hewlett Packard Enterprise Development LP

Manifest = {    
    'Name': 'port_admin_state_monitor_jd',    
    'Description': 'Port Admin Status Monitoring Agent',    
    'Version': '1.0',    
    'Author': 'Aruba Networks mod JD'
}

ParameterDefinitions = {    
    'port_id': {            
        'Name': 'Port Id',        
        'Description': 'Port to be monitored',        
        'Type': 'string',        
        'Default': '1/1/1'    
    }
}
    
class Policy(NAE):    

    def __init__(self):
#Port status        
        uri1 = '/rest/v1/system/ports/{}?attributes=admin'        
        self.m1 = Monitor(            
            uri1,            
            'Port admin status',            
            [self.params['port_id']])        
        self.r1 = Rule('Port disabled administratively')        
        self.r1.condition('transition {} from "up" to "down"', [self.m1])        
        self.r1.action(self.action_port_down)

#Reset policy status when port is up        
        self.r2 = Rule('Port enabled administratively')        
        self.r2.condition('transition {} from "down" to "up"', [self.m1])        
        self.r2.action(self.action_port_up)

    def action_port_down(self, event):        
        ActionSyslog(            
            'Port {} is disabled administratively',            
            [self.params['port_id']])        
        ActionCLI("show lldp configuration {}", [self.params['port_id']])        
        ActionCLI("show interface {} extended", [self.params['port_id']])        
        if self.get_alert_level() != AlertLevel.CRITICAL:            
            self.set_alert_level(AlertLevel.CRITICAL)        
        self.logger.debug("### Critical Callback executed")    
        
    def action_port_up(self, event):        
        self.logger.info("Current alert level: " + str(self.get_alert_level()))        
        if self.get_alert_level() is not None:            
            ActionSyslog(                
                'Port {} is enabled administratively',                
                [self.params['port_id']])           
            self.remove_alert_level()            
            self.logger.debug('Unset the previous status')        
        
        self.logger.debug('### Normal Callback executed')