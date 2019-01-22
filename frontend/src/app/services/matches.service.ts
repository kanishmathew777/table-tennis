import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { BaseWebService } from './base-web.service';
import { Observable } from 'rxjs/Observable';

@Injectable()
export class MatchesService extends BaseWebService {

  matcheslist(): Observable<any> {
    return this.getMethod('matchdetails/matches/');
  }

  matchdetails(id): Observable<any> {
    return this.getMethod(`matchdetails/matches/${id}`);
  }

  setdetails(match_id): Observable<any> {
    return this.getMethod(`matchdetails/sets/?match=${match_id}`);
  }

  setchoices(): Observable<any> {
    return this.getMethod(`set_name_list/`);
  }

  updatescore(data): Observable<any> {
    return this.postMethod(`matchdetails/sets/`, data);
  }

  getsetscore(match_id, set_name): Observable<any> {
    return this.getMethod(`matchdetails/sets/?match=${match_id}&set_name=${set_name}`);
  }
}
