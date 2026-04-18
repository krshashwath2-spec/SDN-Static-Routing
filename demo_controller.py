from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def install(connection, in_port, out_port):
    msg = of.ofp_flow_mod()
    msg.match.in_port = in_port
    msg.actions.append(of.ofp_action_output(port=out_port))
    connection.send(msg)

def _handle_ConnectionUp(event):
    dpid = event.dpid
    con = event.connection

    log.info("Switch %s connected", dpid)

    # s1: h1 <-> s2
    if dpid == 1:
        install(con, 1, 2)
        install(con, 2, 1)

    # s2: s1 <-> s3
    elif dpid == 2:
        install(con, 1, 2)
        install(con, 2, 1)

    # s3: s2 <-> h2
    elif dpid == 3:
        install(con, 1, 3)
        install(con, 3, 1)

    # s4: NOT USED (ignore or optional)
    elif dpid == 4:
        pass

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
