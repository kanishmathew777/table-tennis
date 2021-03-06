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
  public team1_players = null;
  public team2_players = null;
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
    if (this.checkmatchset()) {
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

  matchChange() {
    if (typeof (this.match_score.set_name) !== 'object') {
      this.updateinitialsetscore();
    }
  }

  setChange() {
    if (typeof (this.match_score.match) !== 'object') {
      this.updateinitialsetscore();
    }
  }

  updateinitialsetscore() {
    this.matchservice.getsetscore(this.match_score.match, this.match_score.set_name).subscribe(
      data => {
        this.match_score.team1_score = data.team1_score;
        this.match_score.team2_score = data.team2_score;
        this.team1_players = data.team1_players;
        this.team2_players = data.team2_players;
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

  increment(field) {
    if (field === 'team1') {
      if (this.checkmatchset()) {
        this.match_score.team1_score += 1;
        this.onSubmit();
      }
    } else if (field === 'team2') {
      if (this.checkmatchset()) {
        this.match_score.team2_score += 1;
        this.onSubmit();
      }
    }
  }

  decrement(field) {
    if (field === 'team1') {
      if (this.checkmatchset()) {
        this.match_score.team1_score -= 1;
        this.onSubmit();
      }
    } else if (field === 'team2') {
      if (this.checkmatchset()) {
        this.match_score.team2_score -= 1;
        this.onSubmit();
      }
    }
  }

  getnames(nameslist) {
    return nameslist.join(' / ');
  }

  checkmatchset() {
    if (typeof (this.match_score.match) === 'object' || typeof (this.match_score.set_name) === 'object') {
      this.toastr.error('Match and set required', 'Enter valid match or set', { timeOut: 1000 });
      return false;
    }
    return true;
  }
}
