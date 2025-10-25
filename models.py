class Node:
    def __init__(self, node_id: int, address: str | None = None):
        self.node_id = node_id
        self.address = address
        self.links: list[Link] = []

    def __str__(self):
        connected_nodes = [
            link.node_y.node_id if link.node_x == self else link.node_x.node_id
            for link in self.links
        ]
        return f"ノード(ID: {self.node_id}, アドレス: {self.address}, 接続ノード: {connected_nodes})"

    def add_link(self, link: Link):
        self.links.append(link)


class Link:
    def __init__(
        self,
        node_x: Node,
        node_y: Node,
        bandwidth: int = 10000,
        delay: float = 0.001,
        packet_loss: float = 0.0,
    ):
        self.node_x = node_x
        self.node_y = node_y
        self.bandwidth = bandwidth
        self.delay = delay
        self.packet_loss = packet_loss

        self.node_x.add_link(self)
        self.node_y.add_link(self)

    def __str__(self):
        return (
            f"リンク({self.node_x.node_id} <-> {self.node_y.node_id}, "
            f"帯域幅: {self.bandwidth}, 遅延: {self.delay}, パケットロス率: {self.packet_loss})"
        )
