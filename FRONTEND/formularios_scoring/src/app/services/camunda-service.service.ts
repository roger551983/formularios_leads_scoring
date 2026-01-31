import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '../enviroment/envirment';

@Injectable({
  providedIn: 'root'
})
export class CamundaServiceService {

  //private apiUrl = 'http://localhost:8000/camunda';


  constructor(private http: HttpClient) { }

  iniciarProceso(data: any){

    return this.http.post(
      `${environment.apiURLCamunda}/iniciar-proceso`,
      data
    );
  }
  }

