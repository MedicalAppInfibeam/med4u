# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import serializers
from .models import *



class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields=('doctor_name','doctor_mobile','doctor_description','doctor_address','doctor_speciality','doctor_timings','doctor_pic')

class Doctor_NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor_Note
        fields=('doctor_note','doctor','user')



class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields=('medicine_name','dossage_amt','method','frequency','medicine_date','doctor','usage_instructions','overdose_instructions','possible_sideeffects','brand_names')

class Medicine_NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine_Note
        fields=('medicine_note','medicine','user')
       
 
class BodypartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bodypart
        fields=('medicine','bodypart')

        
class SymptomSerializer(serializers.ModelSerializer):
    medicine = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    bodypart = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Symptom
        fields=('symptom_name','bodypart','medicine','symptom_description','tests')



class Symptom_VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sypmtom_Videos
        fields=('symptom','symptom_video')

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields=('insurance_plan','expiry_date','start_date','user')

        
class ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields=('procedure_name','procedure_description','possible_complication','doctor','user','bodypart','symptom','medicine')

class Procedure_ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure_Images
        fields=('procedure_image','proc')

class Procedure_VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure_Videos
        fields=('procedure_video','proc')


class Procedure_HelplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure_Helpline
        fields=('procedure_help_no','proc')


class Procedure_NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure_Note
        fields=('procedure_note','procedure','user')
        
class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease
        fields=('disease_name','disease_date','symptom','medicine','procedure','user')

        
class Disease_NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disease_Note
        fields=('disease_note','disease','user')

    


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields=('blood_pressure','blood_sugar','cholesterol','height','weight','user','date','notes')

                
                
class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields=('doctor','user','date','time','reason','notes')



class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields=('insurance_plan','expiry_date','start_date','premium','notes','user')




class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields=('doc','notes','user')








       



