import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../enviroment/envirment';

@Injectable({
  providedIn: 'root'
})
export class UploadFileExcelService {

  //private apiURL = 'http://localhost:8000/guardar_excel';

  constructor(private http: HttpClient) {}

  subir_excel(file:File){

    const formData = new FormData();
    formData.append('file',file)

    return this.http.post(environment.apiURLExcel,formData);

  }
}
