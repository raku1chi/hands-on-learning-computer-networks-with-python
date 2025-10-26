from models import Link, NetworkGraph, Node, Packet


def ch01():
    network_graph = NetworkGraph()

    node1 = Node(node_id=1, address="00:01", network_graph=network_graph)
    node2 = Node(node_id=2, address="00:02", network_graph=network_graph)
    link = Link(node_x=node1, node_y=node2, network_graph=network_graph)

    print(node1)
    print(node2)
    print(link)

    node1.send_packet(Packet(src="00:01", dst="00:02", payload="Hello, World!"))
    node2.send_packet(Packet(src="00:02", dst="00:01", payload="Hi there!"))

    for i in range(10):
        node1.send_packet(
            Packet(src="00:01", dst="00:02", payload=f"Packet {i} from Node 1")
        )

    node3 = Node(node_id=3, address="00:03", network_graph=network_graph)
    Link(
        node_x=node2,
        node_y=node3,
        bandwidth=1000000,
        delay=0.01,
        network_graph=network_graph,
    )

    node4 = Node(node_id=4, address="00:04", network_graph=network_graph)
    Link(
        node_x=node2,
        node_y=node4,
        bandwidth=100,
        delay=0.1,
        network_graph=network_graph,
    )

    network_graph.draw()


def main():
    ch01()


if __name__ == "__main__":
    main()
