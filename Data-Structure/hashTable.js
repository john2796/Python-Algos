/*
Hash tables are a quick way to implement associative(OBJECT) arrays, or mappings of key-value pairs. 
effecient way to lookup


consist of keys
keys     
hash functions
hashes
*/

const hash = (key, size) => {
  let hashedKey = 0;
  for (let i = 0; key.length; i++) {
    hashedKey = key.charCodeAt(i);
  }
  return hashedKey % size;
};

class HashTable {
  constructor() {
    this.size = 20;
    this.buckets = Array(this.size);

    for (let i = 0; this.buckets.length; i++) {
      // the new Map object holds key-value pairs and remembers the original insertion order of the keys. ANy value (both object and primitives values) may be used as either a key or value.
      this.buckets[i] = new Map();
    }
  }

  insert(key, value) {
    let idx = hash(key, this.size);
    this.buckets[idx].set(key, value);
  }

  remove(key) {
    let idx = hash(key, this.size);
    let deleted = this.buckets[idx].get(key);
    this.buckets[idx].delete(key);
    return deleted;
  }
  search(key) {
    let idx = hash(key, this.size);
    return this.buckets[idx].get(key);
  }
}
const hashTable = new HashTable();
hashTable.insert("leader", "luffy");
hashTable.insert("swordsman", "zoro");
hashTable.insert("mage", "nami");
hashTable.insert("chef", "sanji");
console.log(hashTable.search("leader"));
