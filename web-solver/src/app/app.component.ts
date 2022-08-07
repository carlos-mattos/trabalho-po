import { Component } from '@angular/core';
import { FormBuilder, FormGroup } from "@angular/forms"
import { SolverService } from "./app.services"

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
})
export class AppComponent {
  inputForm: FormGroup
  spinner: boolean
  timeToExecute: number
  result: any

  constructor(private formBuilder: FormBuilder, private solverService: SolverService) {
    this.buildForm()
    this.spinner = false
    this.result = null
  }

  buildForm() {
    this.inputForm = this.formBuilder.group({
      x1: this.formBuilder.control(0),
      x2: this.formBuilder.control(0)
    })
  }


  async onSubmit() {
    this.spinner = true
    
    this.result = null

    const t1 = Date.now()
    
    const result = await this.solverService.solveProblem(this.inputForm.value)
    
    this.result = result

    const t2 = Date.now()

    this.timeToExecute = t2-t1

    this.spinner = false
  }

}
