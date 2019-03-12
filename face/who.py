from aip import AipFace

conf = json.loads(open('/etc/appid.json').read()) 
client = AipFace(conf["app_id"], conf["api_key"], conf["SECRET_KEY"])



