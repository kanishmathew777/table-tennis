import { Component, OnInit } from '@angular/core';
import { StandingsService } from '../services/standings.service';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-standings',
  templateUrl: './standings.component.html',
  styleUrls: ['./standings.component.scss'],
  providers: [StandingsService],
})
export class StandingsComponent implements OnInit {

  constructor(private standingservice: StandingsService,
    private toaster: ToastrService) { }

  public group_standings = [];

  ngOnInit() {
    this.getstandings();
    setInterval(() => { this.getstandings(); }, 8000);
  }

  getstandings() {
    this.standingservice.standings().subscribe(
      data => {
        console.log('standing:', data);
        this.group_standings = data;
      },
      error => {
        console.log('error', error);
        let error_body = error.error;
        if (!error.status) {
          error_body = 'Failed To connect';
        }
        this.toaster.error('Connection Failed', error_body, { timeOut: 900 });
      }
    );
  }

}
