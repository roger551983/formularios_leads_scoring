import { TestBed } from '@angular/core/testing';

import { UploadFileExcelService } from './upload-file-excel.service';

describe('UploadFileExcelService', () => {
  let service: UploadFileExcelService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(UploadFileExcelService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
