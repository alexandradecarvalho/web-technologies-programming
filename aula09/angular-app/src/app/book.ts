import {Author} from "./author";
import {Publisher} from "./publisher";

export class Book{
  title: string | undefined;
  year: number | undefined;
  authors: Author[] | undefined;
  publisher: Publisher | undefined;
}
