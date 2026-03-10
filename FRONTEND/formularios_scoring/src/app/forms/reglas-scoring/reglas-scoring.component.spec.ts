import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ReglasScoringComponent } from './reglas-scoring.component';

describe('ReglasScoringComponent', () => {
  let component: ReglasScoringComponent;
  let fixture: ComponentFixture<ReglasScoringComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ReglasScoringComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ReglasScoringComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
