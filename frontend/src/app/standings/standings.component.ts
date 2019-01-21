import { Component, OnInit } from '@angular/core';
import { StandingsService } from '../services/standings.service';

@Component({
  selector: 'app-standings',
  templateUrl: './standings.component.html',
  styleUrls: ['./standings.component.scss'],
  providers: [StandingsService],
})
export class StandingsComponent implements OnInit {

  constructor(private standingservice: StandingsService) { }

  public group_standings = [];

  ngOnInit() {
    this.getstandings();
  }

  getstandings() {
    this.standingservice.standings().subscribe(
      data => {
        console.log(data);
        this.group_standings = data;
        // const process_id = data.id;
        // this.spinner.show();
        // this.polling_data(process_id);
      },
      error => {
        console.log('error', error);
        // let error_body = error.error;
        // if (!error.status) {
        //   error_body = 'Failed To connect';
        // }
        // this.toastr.error('Connection Failed', error_body, { timeOut: 900 });
      }
    );
  }

}
