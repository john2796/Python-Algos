class LinkedListNode {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this[head] = null;
  }

  add(data) {
    // create a new node
    const newNode = new LinkedListNode(data);
    // splecia case : no item in the list yet
    if (this[head] === null) {
      // just set the head to the new node
      this[head] = newNode;
    }
    //  start out by looking at the first node;
    let current = this[head];
    //  follow `next` links until you reach the end
    while (current.next !== null) {
      current = current.next;
    }
    //  assign the node into the `next` pointer
    current.next = newNode;
  }
  get(index) {
    // ensure `index` is a positinve value
    if (index > -1) {
      // the pointer to use for traversal
      let current = this[head];
      // used to keep track of where in the list you are
      let i = 0;
      // traverse the list until you reach either the end
      while (current !== null && i < index) {
        current = current.next;
        i++;
      }
      // return the ata if `current` isn't null
      return current !== null ? current.data : undefined;
    } else {
      return undefined;
    }
  }

  *values() {
    let current = this[head];
    while (current !== null) {
      yield current.data;
      current = current.next;
    }
  }
  [Symbol.iterator]() {
    return this.values();
  }
}

const list = new LinkedList();
list.add("red");
list.add("orange");
list.add("yellow");

// get the seoncd item in the list
console.log(list.get(1));

// print out all items
for (const color of list) {
  console.log(color);
}
