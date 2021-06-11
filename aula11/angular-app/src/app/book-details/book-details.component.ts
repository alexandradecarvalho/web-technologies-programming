import { Component, Input, OnInit } from '@angular/core';
import { Book } from "../book";
import { BOOKS } from "../bookslist";

import {ActivatedRoute} from "@angular/router";
import {Location} from "@angular/common";
import {PUBLISHERS} from "../publisherslist";

@Component({
  selector: 'app-book-details',
  templateUrl: './book-details.component.html',
  styleUrls: ['./book-details.component.css']
})
export class BookDetailsComponent implements OnInit {
  @Input() book: Book | undefined;

  constructor(private route: ActivatedRoute, private location: Location) { }

  ngOnInit(): void {
  }

  private getBook() : void {
    // @ts-ignore
    const nam = (str) +this.route.snapshot.params['str'];
    this.book = BOOKS.find( book => book.title === nam);
  }

  goBack() : void{
    this.location.back();
  }

}
