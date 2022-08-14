import { Component } from '@angular/core';
import { SolverService } from "./app.services"
import { NgxFileDropEntry, FileSystemFileEntry, FileSystemDirectoryEntry } from 'ngx-file-drop';
import { ToastrService } from "ngx-toastr"

interface IFilesArray {
  name: string
  lastModified: string
  size: number
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
})
export class AppComponent {
  spinner: boolean
  timeToExecute: number
  files: IFilesArray[] = [];
  formData: FormData

  constructor(private solverService: SolverService, private toastrService: ToastrService) {
    this.spinner = false
    this.formData = new FormData()
  }

  public dropped(files: NgxFileDropEntry[]) {
    for (const droppedFile of files) {
      if (droppedFile.fileEntry.isFile) {
        const fileEntry = droppedFile.fileEntry as FileSystemFileEntry;
        fileEntry.file((file: File) => {

          if (!file.type.includes("csv")) {
            this.toastrService.error("Formato de arquivo inválido", "Erro")
            return
          }

          if(this.files.length > 0){
            this.files = []
          }

          this.files.push({
            lastModified: new Date(file.lastModified).toLocaleDateString('pt-BR'),
            name: file.name,
            size: file.size
          })

          this.formData.append( 'file', new Blob([file], { type: 'text/csv' }), file.name);
        });

      } else {
        const fileEntry = droppedFile.fileEntry as FileSystemDirectoryEntry;
        console.log(droppedFile.relativePath, fileEntry);
      }
    }
  }

  async submitFile(){
    await this.solverService.solveProblem(this.formData)
  }

}
