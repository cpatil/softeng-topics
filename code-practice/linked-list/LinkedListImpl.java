class LinkedList {
	private static class Node<T> {
		private T data;
		private Node<T> next;
	
		public Node(T data, Node<T> head) {
			this.data = data;
			this.next = next;
		}
	}

	private Node<T> head;
	private int size;

	public LinkedList() {
		this.head = null;
	}

	public LinkedList(Node<T> head) {
		this.head = head;
		this.size++;
	}

	public void add(T data) {
		Node<T> node = new Node(data);

		if (this.head == null)
			this.head = node;
		else {
			Node<T> current = this.head;
			while (current.next != null) {
				current = current.next;
			}
			current.next = node;
			this.size++;
		}
	}

	public void remove(T data) {
		
	}
}