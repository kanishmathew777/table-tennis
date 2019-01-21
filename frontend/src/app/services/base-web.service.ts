import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';
import { Router } from '@angular/router';

import 'rxjs/add/operator/map';
import 'rxjs/add/operator/catch';
import 'rxjs/add/observable/throw';


@Injectable()
export class BaseWebService {

  private baseURL = environment.apiUrl;

  constructor(private http: HttpClient, private router: Router) {}

  getMethod(Url: string): Observable<any> {
    return this.http
      .get(this.baseURL + Url)
      .map((res: Response) => res)
      .catch((e: any) => {
        if (e.status === 401) {
            this.router.navigate(['/login']);
            return Observable.throw('401');
        } else {
          return Observable.throw(e);
        }
      });
  }

  postMethod(Url, Data): Observable<any> {
    return this.http
      .post(this.baseURL + Url, Data)
      .map((res: Response) => res)
      .catch((e: any) => {
        if (e.status === 401 && Url !== '/login') {
            this.router.navigate(['/login']);
            return Observable.throw(e);
        } else {
          return Observable.throw(e);
        }
      });
  }

  putMethod(Url, Data): Observable<any> {
    return this.http
      .put(this.baseURL + Url, Data)
      .map((res: Response) => res)
      .catch((e: any) => {
        if (e.status === 401) {
            this.router.navigate(['/login']);
            return Observable.throw(e);
        } else {
          return Observable.throw(e);
        }
      });
  }

  deleteMethod(Url): Observable<any> {
    return this.http
      .delete(this.baseURL + Url)
      .map((res: Response) => res)
      .catch((e: any) => {
        if (e.status === 401) {
            this.router.navigate(['/login']);
            return Observable.throw(e);
        } else {
          return Observable.throw(e);
        }
      });
  }

  getMethodBlob(Url): Observable<any> {
    return this.http
      .get(this.baseURL + Url, { responseType: 'blob' });
  }


  getErrorMessage(error) {
    if (typeof error.detail === 'string' || error.detail instanceof String) {
        return error.detail;
    }

  }

}
