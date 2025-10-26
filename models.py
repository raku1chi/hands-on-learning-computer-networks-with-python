import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


class NetworkGraph:
    def __init__(self):
        self.graph: nx.Graph[Node] = nx.Graph()

    def add_node(self, node: Node, label: str | None = None):
        self.graph.add_node(node, label=label)

    def add_link(
        self,
        node_x: Node,
        node_y: Node,
        label: str | None = None,
        bandwidth: int = 10000,
        delay: float = 0.001,
    ):
        self.graph.add_edge(
            node_x, node_y, label=label, bandwidth=bandwidth, delay=delay
        )

    def draw(self):
        def get_edge_width(bandwidth: int) -> float:
            return np.log10(bandwidth) + 1

        def get_edge_color(delay: float) -> str:
            if delay <= 0.001:
                # 1ms以下
                return "green"
            elif delay <= 0.01:
                # 1-10ms
                return "yellow"
            else:
                # 10ms以上
                return "red"

        pos = nx.spring_layout(self.graph)
        edge_widths = [
            get_edge_width(data["bandwidth"])
            for _, _, data in self.graph.edges(data=True)
        ]
        edge_colors = [
            get_edge_color(data["delay"]) for _, _, data in self.graph.edges(data=True)
        ]

        nx.draw(
            self.graph,
            pos,
            with_labels=False,
            node_color="lightblue",
            edge_color=edge_colors,
            width=edge_widths,
        )
        nx.draw_networkx_labels(
            self.graph,
            pos,
            labels=nx.get_node_attributes(self.graph, "label"),  # pyright: ignore[reportUnknownMemberType]
        )
        nx.draw_networkx_edge_labels(
            self.graph,
            pos,
            edge_labels=nx.get_edge_attributes(self.graph, "label"),  # pyright: ignore[reportUnknownMemberType]
        )
        plt.show()  # pyright: ignore[reportUnknownMemberType]


class Node:
    def __init__(
        self,
        node_id: int,
        address: str | None = None,
        network_graph: NetworkGraph | None = None,
    ):
        self.node_id = node_id
        self.address = address
        self.links: list[Link] = []
        self.network_graph = network_graph

        if self.network_graph:
            self.network_graph.add_node(
                self, label=f"Node {self.node_id}\n{self.address}"
            )

    def __str__(self):
        connected_nodes = [
            link.node_y.node_id if link.node_x == self else link.node_x.node_id
            for link in self.links
        ]
        return f"ノード(ID: {self.node_id}, アドレス: {self.address}, 接続ノード: {connected_nodes})"

    def add_link(self, link: Link):
        self.links.append(link)

    def send_packet(self, packet: Packet):
        if packet.dst == self.address:
            self.receive_packet(packet)
            return
        for link in self.links:
            next_node = link.node_y if link.node_x == self else link.node_x
            print(
                f"ノード {self.node_id} からノード {next_node.node_id} へパケットを送信"
            )
            link.transfer_packet(packet, from_node=self)
            break

    def receive_packet(self, packet: Packet):
        print(f"ノード {self.node_id} でパケットを受信: {packet.payload}")


class Link:
    def __init__(
        self,
        node_x: Node,
        node_y: Node,
        bandwidth: int = 10000,
        delay: float = 0.001,
        packet_loss: float = 0.0,
        network_graph: NetworkGraph | None = None,
    ):
        self.node_x = node_x
        self.node_y = node_y
        self.bandwidth = bandwidth
        self.delay = delay
        self.packet_loss = packet_loss
        self.network_graph = network_graph

        self.node_x.add_link(self)
        self.node_y.add_link(self)

        if self.network_graph:
            self.network_graph.add_link(
                node_x,
                node_y,
                f"{bandwidth / 1000000} Mbps, {delay} s",
                self.bandwidth,
                self.delay,
            )

    def __str__(self):
        return (
            f"リンク({self.node_x.node_id} <-> {self.node_y.node_id}, "
            f"帯域幅: {self.bandwidth}, 遅延: {self.delay}, パケットロス率: {self.packet_loss})"
        )

    def transfer_packet(self, packet: Packet, from_node: Node):
        next_node = self.node_y if from_node == self.node_x else self.node_x
        next_node.receive_packet(packet)


class Packet:
    def __init__(self, src: str, dst: str, payload: str):
        self.src = src
        self.dst = dst
        self.payload = payload

    def __str__(self):
        return f"パケット(送信元: {self.src}, 宛先: {self.dst}, ペイロード: {self.payload})"
