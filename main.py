from models import Link, NetworkGraph, Node, Packet


def main():
    network_graph = NetworkGraph()

    node1 = Node(node_id=1, address="00:01", network_graph=network_graph)
    node2 = Node(node_id=2, address="00:02", network_graph=network_graph)
    link = Link(node_x=node1, node_y=node2, network_graph=network_graph)

    print(node1)
    print(node2)
    print(link)

    packet = Packet(src="00:01", dst="00:02", payload="Hello, World!")
    node1.send_packet(packet)

    network_graph.draw()


if __name__ == "__main__":
    main()
