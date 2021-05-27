import { NgModule } from '@angular/core';
import { RouterModule, Routes } from "@angular/router";

import { CommonModule } from '@angular/common';
import { AuthorsComponent } from "./authors/authors.component";
import {OverviewComponent} from "./overview/overview.component";
import {AuthorDetailsComponent} from "./author-details/author-details.component";

const routes: Routes = [
  {path: 'authors', component: AuthorsComponent},
  {path: 'overview', component: OverviewComponent},
  {path: 'authordetails/:num', component: AuthorDetailsComponent},
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
