print('-------------------------------------------------------|')
print('-------WELCOME TO THE HOMEOPATHIC EXPERT SYSTEM--------|')
print('Enter Category of Diagnosis                            |')
print('1.Pediatric                                            |')
print('2.Digestive                                            |')
print('3.Fever and general                                    |')
print('4.Joints and muscles                                   |')
print('5.Respiratory diseases                                 |')
print('6.Skin diseases                                        |')
print('7.Lifestyle diseases                                   |')
print('-------------------------------------------------------|')
b=[]

while(1):
    print()
    a=int(input('Enter category number: '))
    print()

    if(a==1):
        print('Symptoms: ')
        print('1. Headache')
        print('2. Runny Nose')
        print('3. Fever')
        print('4. Shortness of Breath')
        print('5. Stomach Ache')
        print('6. Vomiting')
        print('7. Cough')

        b1=input('Enter symptom number: ').split(' ')
        if '1' in b1:
             b.append('KINDIVAL')
        if '2' in b1:
             b.append('ENUKIND')
        if '3' in b1:
             b.append('NISIKIND')
        if '4' in b1:
             b.append('ANEKIND')
        if '5' in b1:
             b.append('ECHINACEA ANGUSTIFOLIA 1X')
        if '6' in b1:
             b.append('CALCIOKIND')
        if '7' in b1:
             b.append('TUSSIKIND')

        print('The count is ',len(b))
        print('The medicine list is ',b)
        print('Even after medication you are not comfortable. Please consult a doctor. Thank you.')
        break

    elif(a==2):
        print('Enter the symptoms: ')
        print('1. Diarrhoea')
        print('2. Vomiting')
        print('3. Acidity')
        print('4. Colic')
        print('5. Nausea')
        print('6. Motion sickness')
        print('7. Loss of apetite')
        print('8. Irritable Bowels')
        print('9. Constipation')
        print('10. Dysentry')

        b1=input('Enter symptom number: ').split()
        if '1' in b1:
            b.append('BIOCOMBINATION NO. 08')
        if '2' in b1:
            b.append('ALPHA-MS')
        if '3' in b1:
            b.append('ALPHA-ACID')
        if '4' in b1:
            b.append('COLIKIND')
        if '5' in b1:
            b.append('KINDIGEST')
        if '6' in b1:
            b.append('ALPHA-MS')
        if '7' in b1:
            b.append('ALPHA-LIV')
        if '8' in b1:
            b.append('ALPHA-MS')
        if '9' in b1:
            b.append('NATRUM MURIATICUM')
        if '10' in b1:
            b.append('HOLARRHENA ANTIDYSENTERICA 1X')
        print('The count is ',len(b))
        print('The list is ',b)
        print('Even after medication, you are not comfortable. Please consult a doctor. Thank you.')
        break

    elif(a==3):
        print('Symptoms:')
        print('1. Fever')
        print('2. Fatigue')
        print('3. Tonsilities')
        print('4. Nausea')
        print('5. Chills')
        print('6. Cold')
        print('7. Cough')

        b1=input('Enter symptom number: ').split()
        if '1' in b1:
            b.append('ACONITUM PENTARKAN')
        if '2' in b1:
              b.append('MUNOSTIM')
        if '3' in b1:
              b.append('ALPHA-TONS')
        if '4' in b1:
            b.append('ALPHA-LIV')
        if '5' in b1:
              b.append('ALPHA-WD')
        if '6' in b1:
              b.append('NUSIKIND')
        if '7' in b1:
             b.append('TUSSIKIND')
        print('The count is ',len(b))
        print('The medicine list is ',b)
        print('Even after medication, you are not comfortable. Please consult a doctor. Thank you.')
        break
    
    elif(a==4):
        print('Enter the symptoms: ')
        print('1. Cramps')
        print('2. Muscular pain')
        print('3. Rheumatic pain')
        print('4. Bone problems')
        print('5. Body ache')
        print('6. Joints')
        print('7. Inflammation')
        print('8. Muscles')
        print('9. Spasms')
        print('10. Osteoarthritis')

        b1=input('Enter symptom number: ').split()
        if '1' in b1:
            b.append('MAGNESIUM PHOSPHORICUM')
        if '2' in b1:
            b.append('Alpha-MP')
        if '3' in b1:
            b.append('Alpha-MP')
        if '4' in b1:
            b.append('Calcarea phosphorica')
        if '5' in b1:
            b.append('TOPI ARNICA CREAM')
        if '6' in b1:
            b.append('Topi MP Gel')
        if '7' in b1:
            b.append('Topi Heal Cream')
        if '8' in b1:
            b.append('Kali phosphoricum')
        if '9' in b1:
            b.append('Magnesium Phosphoricum Pentarkan')
        if '10' in b1:
            b.append('Biocombination No. 19')
        print('The count is ',len(b))
        print('The list is ',b)
        print('Even after medication, you are not comfortable. Please consult a doctor. Thank you.')
        break

    elif(a==5):
        print('Symptoms: ')
        print('1. Chronic Cough')
        print('2. Spasmodic cough')
        print('3. Whooping Cough')
        print('4. Irritating Cough')
        print('5. Nasal Congestion')
        print('6. Sneezing')
        print('7. Stuffy nose')
        print('8. Breathlessness')
        print('9. Coryza')
        print('10. Respiratory Congestion')

        b1=input('Enter symptom number: ').split()
        if '1' in b1:
            b.append('Alpha-CC')
        if '2' in b1:
            b.append('Alpha-Coff')
        if '3' in b1:
            b.append('Aconitum Pentarkan')
        if '4' in b1:
            b.append('Glycyrrhiza glabra 1X')
        if '5' in b1:
            b.append('Alpha-NC')
        if '6' in b1:
            b.append('Alpha-RC')
        if '7' in b1:
            b.append('Alpha-NC2')
        if '8' in b1:
            b.append('Alpha-RC1')
        if '9' in b1:
            b.append('BIOCOMBINATION NO. 05')
        if '10' in b1:
            b.append('Biocombination No. 13')
        print('the count is ',len(b))
        print('the list is ',b)
        print('Even after medication, you are not comfortable. Please consult a doctor. Thank you.')
        break

    elif(a==6):
        print('Symptoms: ')
        print('1. Acne')
        print('2. Pimples')
        print('3. Psoriasis')
        print('4. Bed sores')
        print('5. Boils')
        print('6. Cuts')
        print('7. Itching')
        print('8. Scabies')
        print('9. Dermatities')
        print('10. Fungal Infection')

        b1=input('Enter symptom number: ').split()
        if '1' in b1:
            b.append('TOPI BERBERIS CREAM')
        if '2' in b1:
            b.append('Calcarea sulphurica')
        if '3' in b1:
            b.append('Alpha-WD')
        if '4' in b1:
            b.append('Topi Heal Cream')
        if '5' in b1:
            b.append('Silicea')
        if '6' in b1:
            b.append('Hepar Sulphuris Pentarkan')
        if '7' in b1:
            b.append('Graphites Pentarkan')
        if '8' in b1:
            b.append('Topi Sulphur Cream')
        if '9' in b1:
            b.append('B&T Akne - Sor Soap')
        if '10' in b1:
            b.append('B&T CALENDULA & ALOE VERA MULTIPURPOSE CREAM')
        print('The count is ',len(b))
        print('The list is ',b)
        print('Even after medication, you are not comfortable. Please consult a doctor. Thank you.')
        break

    elif(a==7):
         print('Symptoms: ')
         print('1. Weight loss')
         print('2. Stress')
         print('3. Insomnia')
         print('4. Hair greying')
         print('5. Hyper tension')
         print('6. Burnout')
         print('7. Obesity')
         print('8. Alcoholism')
         print('9. Thyroid Disorder')
         print('10. Weakness')

         b1=input('Enter symptom number: ').split()
         if '1' in b1:
            b.append('Phytolacca Berry Tablets')
         if '2' in b1:
            b.append('Alpha-TS')
         if '3' in b1:
            b.append('Kali phosphoricum')
         if '4' in b1:
            b.append('Damiaplant')
         if '5' in b1:
            b.append('Essentia aurea')
         if '6' in b1:
            b.append('Ginseng 1X')
         if '7' in b1:
            b.append('Phytolacca Berry Tablets*')
         if '8' in b1:
            b.append('Quercus robur 1x')
         if '9' in b1:
            b.append('Thyroidinum 3X (LATT)')
         if '10' in b1:
            b.append('Biocombination No. 03')
         print('The count is ',len(b))
         print('The list is ',b)
         print('Even after medication, you are not comfortable. Please consult a doctor. Thank you.')
         break

    else:
        print('please enter a valid option')