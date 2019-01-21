import { Injectable } from '@angular/core';
import { BaseWebService } from './base-web.service';
import { Observable } from 'rxjs/Observable';

@Injectable()
export class LoginService extends BaseWebService {

  login(data): Observable<any> {
    return this.postMethod('api-token-auth/', data);
  }
}
