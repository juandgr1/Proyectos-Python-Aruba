session_dict = dict(s=session.login(base_url, username, password), url=base_url)

system_info_dict = system.get_system_info(params={"selector": "configuration"}, **session_dict)

pprint.pprint(system_info_dict)