import { Injectable } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';

@Injectable()
export class AuthService {

  constructor(private cookieService: CookieService) { }

  public isAuthenticated(): boolean {
    const cookieExists: boolean = this.cookieService.check('token');
    return cookieExists;
  }

}
