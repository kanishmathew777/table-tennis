import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { BaseWebService } from './base-web.service';
import { Observable } from 'rxjs/Observable';

@Injectable()
export class StandingsService extends BaseWebService {

  standings(): Observable<any> {
    return this.getMethod('userdetails/groups/');
  }

}
