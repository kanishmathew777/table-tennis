import { TestBed, inject } from '@angular/core/testing';

import { BaseWebService } from './base-web.service';

describe('BaseWebService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [BaseWebService]
    });
  });

  it('should be created', inject([BaseWebService], (service: BaseWebService) => {
    expect(service).toBeTruthy();
  }));
});
