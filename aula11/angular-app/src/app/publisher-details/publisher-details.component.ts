import {Component, Input, OnInit} from '@angular/core';
import { Publisher } from "../publisher";
import { PUBLISHERS } from "../publisherslist";

import {ActivatedRoute} from "@angular/router";
import {Location} from "@angular/common";

@Component({
  selector: 'app-publisher-details',
  templateUrl: './publisher-details.component.html',
  styleUrls: ['./publisher-details.component.css']
})
export class PublisherDetailsComponent implements OnInit {
  @Input() publisher : Publisher | undefined;

  constructor( private route: ActivatedRoute, private location: Location) { }

  ngOnInit(): void {
    this.getPublisher();
  }

  private getPublisher() : void {
    // @ts-ignore
    const nam = (str) +this.route.snapshot.params['str'];
    this.publisher = PUBLISHERS.find( publisher => publisher.name === nam);
  }

  goBack() : void{
    this.location.back();
  }
}
