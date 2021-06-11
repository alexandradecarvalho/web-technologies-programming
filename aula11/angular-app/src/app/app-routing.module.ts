import { NgModule } from '@angular/core';
import { RouterModule, Routes } from "@angular/router";

import { CommonModule } from '@angular/common';
import { AuthorsComponent } from "./authors/authors.component";
import { PublishersComponent } from "./publishers/publishers.component";
import { BooksComponent } from "./books/books.component";
import {OverviewComponent} from "./overview/overview.component";
import {AuthorDetailsComponent} from "./author-details/author-details.component";
import {PublisherDetailsComponent} from "./publisher-details/publisher-details.component";
import {BookDetailsComponent} from "./book-details/book-details.component";

const routes: Routes = [
  {path: 'authors', component: AuthorsComponent},
  {path: 'publishers', component: PublishersComponent},
  {path: 'books', component: BooksComponent},
  {path: 'overview', component: OverviewComponent},
  {path: 'authordetails/:num', component: AuthorDetailsComponent},
  {path: 'publisherdetails/:str', component: PublisherDetailsComponent},
  {path: 'bookdetails/:str', component: BookDetailsComponent},
]

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    RouterModule.forRoot(routes)
  ],
  exports: [
    RouterModule
  ]
})
export class AppRoutingModule { }
