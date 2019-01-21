import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ToastrService } from 'ngx-toastr';
import { NgxSpinnerService } from 'ngx-spinner';
import { CookieService } from 'ngx-cookie-service';
import { Router } from '@angular/router';
import { LoginService } from '../services/login.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
  providers: [LoginService],
})
export class LoginComponent implements OnInit {

  loginForm: FormGroup;
  submitted: boolean;

  constructor(
    private formBuilder: FormBuilder,
    private spinner: NgxSpinnerService,
    private toastr: ToastrService,
    private cookieService: CookieService,
    private router: Router,
    private loginService: LoginService,
  ) {
    this.loginForm = this.formBuilder.group({
      username: ['', Validators.required],
      password: ['', Validators.required]
    });
    this.submitted = false;
  }

  ngOnInit() {
  }

  login() {
    this.submitted = true;
    if (this.loginForm.valid) {
      this.spinner.show();
      const data = {
        username: this.loginForm.value.username,
        password: this.loginForm.value.password
      };
      this.loginService.login(data).subscribe(
        response => {
          this.spinner.hide();
          console.log(response.token);
          this.cookieService.set('token', response.token);
          this.toastr.success('Logged in successfully', '', { timeOut: 1000 });
          this.router.navigate(['/updatescore/']);
        },
        error => {
          this.spinner.hide();
          this.cookieService.delete('token');
          this.toastr.error(error.error.detail, 'Login Failed', { timeOut: 3000 });
          console.error(error);
        }
      );
    }
  }

}
