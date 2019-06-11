//----------------- binary search js implementation ----------------

const binary_search = (arr, target) => {
  let low = 0;
  let high = arr.length - 1;

  while (low <= high) {
    // get mid and value
    let mid = Math.round(low + high / 2);
    // case 1 when we found match
    if (arr[mid] == target) {
      return arr[mid];
    }
  }
};

const arr = [1, 2, 3, 4, 5, 6];
binary_search(arr, 6);
