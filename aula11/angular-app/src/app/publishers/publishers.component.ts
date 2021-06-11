import { Component, OnInit } from '@angular/core';
import {Publisher} from "../publisher";
import {PUBLISHERS} from "../publisherslist";

@Component({
  selector: 'app-publishers',
  templateUrl: './publishers.component.html',
  styleUrls: ['./publishers.component.css']
})
export class PublishersComponent implements OnInit {

  publishers: Publisher[] | undefined;
  selectedPublisher: Publisher | undefined;

  constructor() {
    this.publishers = PUBLISHERS;
  }

  ngOnInit(): void {
  }

  onSelect(publisher: Publisher): void {
    this.selectedPublisher = publisher;
  }
}
