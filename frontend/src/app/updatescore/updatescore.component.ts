import { Component, OnInit } from '@angular/core';
import { MatchesService } from '../services/matches.service';
import { ToastrService } from 'ngx-toastr';
import { UpdateScore } from './updatescore.interface';

@Component({
  selector: 'app-updatescore',
  templateUrl: './updatescore.component.html',
  styleUrls: ['./updatescore.component.scss'],
  providers: [MatchesService],
})
export class UpdatescoreComponent implements OnInit {

  public matchlist = [];
  public setlist = [];
  constructor(
    private matchservice: MatchesService,
    private toastr: ToastrService,
  ) { }

  match_score = new UpdateScore([], [], 0, 0);

  ngOnInit() {
    this.getMatches();
    this.getSets();
  }

  getMatches() {
    this.matchservice.matcheslist().subscribe(
      data => {
        this.matchlist = data;
      },
      error => {
        let error_body = error.error;
        if (!error.status) {
          error_body = 'Failed To connect';
        }
        this.toastr.error('Connection Failed', error_body, { timeOut: 900 });
      }
    );
  }

  onSubmit() {
    if (typeof(this.match_score.match) === 'object' || typeof(this.match_score.set) === 'object') {
      this.toastr.error('Match and set required', 'Enter valid match or set', { timeOut: 1000 });
    } else {
      this.matchservice.updatescore(this.match_score).subscribe(
        data => {
          this.toastr.success('Successfull', 'Updated Successfully', { timeOut: 400 });
        },
        error => {
          let error_body = error.error;
          if (!error.status) {
            error_body = 'Failed To connect';
          }
          this.toastr.error('Connection Failed', error_body, { timeOut: 900 });
        }
      );
    }
    console.log(this.match_score);
  }

  getSets() {
    this.matchservice.setchoices().subscribe(
      data => {
        this.setlist = data;
      },
      error => {
        let error_body = error.error;
        if (!error.status) {
          error_body = 'Failed To connect';
        }
        this.toastr.error('Connection Failed', error_body, { timeOut: 900 });
      }
    );
  }
}
