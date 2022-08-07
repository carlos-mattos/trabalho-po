import { Component } from '@angular/core';
import { FormBuilder, FormGroup } from "@angular/forms"
import { CarService } from "./app.services"

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
})
export class AppComponent {
  inputForm: FormGroup

  constructor(private formBuilder: FormBuilder, private carService: CarService) {
    this.buildForm()
  }

  buildForm() {
    this.inputForm = this.formBuilder.group({
      x1: this.formBuilder.control(0),
      x2: this.formBuilder.control(0)
    })
  }


  onSubmit() {
    console.log(this.inputForm.value)
    this.carService.getCars()
  }

}
