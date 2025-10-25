from models import Node


def main():
    node1 = Node(node_id=1, address="00:01")
    node2 = Node(node_id=2, address="00:02")

    print(node1)
    print(node2)


if __name__ == "__main__":
    main()
