import { Component, OnInit, ViewChild } from '@angular/core';
import { MatchesService } from '../services/matches.service';
import { ToastrService } from 'ngx-toastr';


@Component({
  selector: 'app-matches',
  templateUrl: './matches.component.html',
  styleUrls: ['./matches.component.scss'],
  providers: [MatchesService],
})
export class MatchesComponent implements OnInit {

  @ViewChild('match') matchnumber: any;

  constructor(private toastr: ToastrService, private matchservice: MatchesService) { }
  public matchlist = [];
  public matchdata = null;
  public setdata = null;
  public match_index = 0;
  private processCompletionId: any = 0;

  private set_status = {
    1: 'COMPLETED',
    2: 'LIVE',
    3: 'SCHEDULED'
  };

  ngOnInit() {
    this.getMatches();
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


  matchChange(match_id) {
    console.log(this.matchnumber.nativeElement.value);
    clearInterval(this.processCompletionId);
    if (this.matchnumber.nativeElement.value === 'default_select') {
      this.toastr.error('Please select a match', 'Select match');
      this.matchdata = null;
      this.setdata = null;
    } else {
      this.matchservice.matchdetails(match_id).subscribe(
        data => {
          this.matchdata = data;
          console.log(this.matchdata);
          this.getsetdata(this.matchdata['id']);
          if (this.matchdata['match_status'] === 2) {
            console.log('start hitting');
            this.updatesets(this.matchdata['id']);
          }
        },
        error => {
          console.log('error', error);
          let error_body = error.error;
          if (!error.status) {
            error_body = 'Failed To connect';
          }
          this.toastr.error('Connection Failed', error_body, { timeOut: 900 });
        }
      );
    }
  }

  private updatesets(matchid): any {
    this.processCompletionId = setInterval(() => { this.getsetdata(matchid, true); }, 5000);
  }

  getsetdata(matchid, checking?) {
    this.matchservice.setdetails(matchid).subscribe(
      data => {
        this.setdata = data;
        if (checking === true) {
          if (this.setdata.match_status === 1 || this.setdata.match_status === 3) {
            this.matchdata.match_status = this.setdata.match_status;
            clearInterval(this.processCompletionId);
            console.log('stopped hitting');
          }
        }
        console.log(this.setdata);
      },
      error => {
        console.log('error', error);
        let error_body = error.error;
        if (!error.status) {
          error_body = 'Failed To connect';
        }
        this.toastr.error('Connection Failed', error_body, { timeOut: 900 });
      }
    );
  }

  getnames(nameslist) {
    return nameslist.join(' / ');
  }

  show_status(status_id) {
    return this.set_status[status_id];
  }

}
