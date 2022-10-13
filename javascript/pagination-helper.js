// Pagination Helper - 5 kyu
// TODO: complete this object/class

// The constructor takes in an array of items and a integer indicating how many
// items fit within a single page
class PaginationHelper {
	constructor(collection, itemsPerPage) {
		this.collection = collection
		this.itemsPerPage = itemsPerPage
	}

	// returns the number of items within the entire collection
	itemCount() {
		this.length = this.collection.length
		return this.length
		//return (this.collection).length
	}

	// returns the number of pages
	// divides total number of items by items per page, then rounds up to account for any remainder
	pageCount() {
		this.pages = Math.ceil(this.itemCount() / this.itemsPerPage)
		return this.pages
	}

	// returns the number of items on the current page. page_index is zero based.
	// this method should return -1 for pageIndex values that are out of range
	pageItemCount(pageIndex) {
		// if the index is higher than the page count
		this.lastPageIndex = this.pageCount() - 1
		if (pageIndex > this.lastPageIndex) {
			return -1
		}
		// if it's the last page
		else if (pageIndex === this.lastPageIndex) {
			if (this.itemCount % this.itemsPerPage === 0) {
				return this.itemsPerPage
			}
			else {
				return this.itemCount() % this.itemsPerPage
			}
		}
		// if it's any page, up to but not including the last page
		else if (pageIndex >= 0) {
			return this.itemsPerPage
		}
		
	}
	// determines what page an item is on. Zero based indexes
	// this method should return -1 for itemIndex values that are out of range
	pageIndex(itemIndex) {
		this.lastItemIndex = this.itemCount() - 1
		// if it's the first item
		if (itemIndex === 0 && this.pageCount() > 0) {
			return 0
		}
		// if index is too high
		else if (itemIndex > this.lastItemIndex || itemIndex < 0) {
			console.log(`${itemIndex} is invalid`)
			return -1
		}
		// if it's the last item
		else if (itemIndex === this.lastItemIndex) {
			console.log(`${itemIndex} is on the last page`)
			return this.pageCount()-1
		}
		// checking every item between first and last
		else if (itemIndex > -1) {
			for (let i = this.pageCount()-1; i >= 0; i--) {
			// we check for first page that is greater than itemIndex - page AFTER where item would be indexed
				if (itemIndex > (this.itemsPerPage * i)) {
					console.log(`item with index ${itemIndex} is on page ${i}`)
					console.log(i)
					return i
				}
			}
		}
	}
}


var helper = new PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4);
//console.log(helper.pageCount())
//console.log(helper.itemCount())
//console.log(helper.pageItemCount(0))
//console.log(helper.pageItemCount(1))
//console.log(helper.pageItemCount(2))
// console.log(helper.pageIndex(5))
// console.log(helper.pageIndex(2))
// console.log(helper.pageIndex(0))
//console.log(helper.pageIndex(20))
//console.log(helper.pageIndex(-10))
// console.log(helper.pageIndex(4))

let list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
var helper2 = new PaginationHelper(list2, 10)
console.log(helper2.pageIndex(22))

