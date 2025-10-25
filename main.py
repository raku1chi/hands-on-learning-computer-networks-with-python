from models import Link, Node, Packet


def main():
    node1 = Node(node_id=1, address="00:01")
    node2 = Node(node_id=2, address="00:02")
    link = Link(node_x=node1, node_y=node2)

    print(node1)
    print(node2)
    print(link)

    packet = Packet(src="00:01", dst="00:02", payload="Hello, World!")
    node1.send_packet(packet)


if __name__ == "__main__":
    main()
