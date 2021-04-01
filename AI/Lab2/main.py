from console.ui import UI
from serv.service import *
from utils.operation import *
repo = Repository()
op = Operation()
g = repo.getGraph()

# for v in g:
#         for w in v.get_connections():
#             vid = v.get_id()
#             wid = w.get_id()
#             print ('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))
#
# print("^ Graph edges with weights ^")

service = Service(repo,op)
ui = UI(service)

ui.showMenu()