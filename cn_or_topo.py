from mininet.topo import Topo

class CN_OR_Topo(Topo):
    def build(self):

        h1 = self.addHost('h1')
        h2 = self.addHost('h2')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')

        # Links
        self.addLink(h1, s1)

        self.addLink(s1, s2)
        self.addLink(s2, s3)

        self.addLink(s1, s4)
        self.addLink(s4, s3)

        self.addLink(s3, h2)

topos = {'cn_or': CN_OR_Topo}
