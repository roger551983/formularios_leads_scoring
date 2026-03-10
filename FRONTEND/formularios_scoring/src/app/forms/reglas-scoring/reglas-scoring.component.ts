import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { UploadFileExcelService } from '../../services/upload-file-excel.service';
import { CamundaServiceService } from '../../services/camunda-service.service';
import { environment } from '../../enviroment/envirment';
@Component({
  selector: 'app-reglas-scoring',
  imports: [CommonModule,FormsModule],
  templateUrl: './reglas-scoring.component.html',
  styleUrl: './reglas-scoring.component.css'
})
export class ReglasScoringComponent {

  ingresos!:number;
  ratioDeuda!: number;
  scoreBuro!: number;
 // processDefinitionId:string="scoring_client";
  archivoSeleccionado!:File;
  nombreArchivo:string|null=null;

  constructor(private excelScoring :UploadFileExcelService,private camundaScoring:CamundaServiceService){}

  onFileSelected(event: Event) {

    const input = event.target as HTMLInputElement;

    if (input.files && input.files.length > 0) {
      this.archivoSeleccionado = input.files[0];
      this.nombreArchivo = this.archivoSeleccionado.name;
    }
  }

  ejecutar() {

    const payload_scoring = {
    processDefinitionId: environment.processDefinitionId,
    variables: {
      ingresos: this.ingresos,
      ratioDeuda: this.ratioDeuda,
      scoreBuro: this.scoreBuro
    }
  };
    console.log(
        payload_scoring
    );

    this.excelScoring.subir_excel(this.archivoSeleccionado)
     .subscribe({
    next: (resp) => {
      console.log('Respuesta:', resp);
      
    },
    error: (err) => {
      console.error(err);
      alert('Error al ejecutar');
    }
  });
  this.camundaScoring.iniciarProceso(payload_scoring)
    .subscribe({
     next: (resp) => {
      console.log('Respuesta:', resp);
      
    },
    error: (err) => {
      console.error(err);
      alert('Error al ejecutar');
    }

});
  }
  



}
