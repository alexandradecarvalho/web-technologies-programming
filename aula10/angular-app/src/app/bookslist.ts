import {Book} from "./book";
import {AUTHORS} from "./authorslist";
import {PUBLISHERS} from "./publisherslist";

export const BOOKS: Book[] = [
  {title:"Cartas de Amor Ophelia Queiroz", year: 1920, authors: [AUTHORS[0]], publisher: PUBLISHERS[0]},
  {title:"Harry Potter and the Philosopher's Stone", year: 2001, authors: [AUTHORS[1]], publisher: PUBLISHERS[1]},
  {title:"IT", year: 1986, authors: [AUTHORS[2]], publisher: PUBLISHERS[2]},
  {title:"The Adventures of Sherlock Holmes", year: 1892, authors: [AUTHORS[3]], publisher: PUBLISHERS[3]},
  {title:"The Fault in Our Stars", year: 2012, authors: [AUTHORS[4]], publisher: PUBLISHERS[4]},
];
