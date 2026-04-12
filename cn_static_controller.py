from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def install_flow(connection, in_port, out_port):
    msg = of.ofp_flow_mod()
    msg.match.in_port = in_port
    msg.actions.append(of.ofp_action_output(port=out_port))
    connection.send(msg)

def _handle_ConnectionUp(event):
    dpid = event.dpid
    connection = event.connection

    log.info("Switch %s connected", dpid)

    # s1 (dpid=1)
    if dpid == 1:
        install_flow(connection, 1, 3)
        install_flow(connection, 3, 1)

    # s4 (dpid=4)
    elif dpid == 4:
        install_flow(connection, 1, 2)
        install_flow(connection, 2, 1)

    # s3 (dpid=3)
    elif dpid == 3:
        install_flow(connection, 2, 3)
        install_flow(connection, 3, 2)

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
