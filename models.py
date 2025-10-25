class Node:
    """ネットワーク内のノードを表すクラス"""

    def __init__(self, node_id: int, address: str | None = None):
        """ノードの初期化
        Args:
            node_id (int): ノードの識別子
            address (str | None): ノードのアドレス (デフォルトは None)
        """
        self.node_id = node_id
        self.address = address

    def __str__(self):
        return f"ノード(ID: {self.node_id}, アドレス: {self.address})"
