
// document.addEventListener('DOMContentLoaded', () => {

  var g_obj_carousel_model = {
    "indexPosA": 0,
    "indexPosB": 0,
    "indexPosC": 0
  }

  const plusSlides = (index, nivel) => {

    const classesArrayA = [
      "client_A_class_1",
      "client_A_class_2",
      "client_A_class_3",
      "client_A_class_4",
      "client_A_class_5",
      ];

    const classesArrayB = [
      "client_B_class_1",
      "client_B_class_2",
      "client_B_class_3",
      "client_B_class_4",
      "client_B_class_5",
      ];

    const classesArrayC = [
      "client_C_class_1",
      "client_C_class_2",
      "client_C_class_3",
      "client_C_class_4",
      "client_C_class_5",
      ];

    let classesArray = null
    let keyPos = null

    if(nivel === 1) {
      classesArray = classesArrayA
      keyPos = "indexPosA"
    }
    else if(nivel === 2) {
      classesArray = classesArrayB
      keyPos = "indexPosB"
    }
    else if(nivel === 3) {
      classesArray = classesArrayC
      keyPos = "indexPosC"
    }
      
    const clientDataOld = document.getElementById(`${classesArray[g_obj_carousel_model[keyPos]]}`);

    if ( (g_obj_carousel_model[keyPos] === classesArray.length - 1) & (index != -1))
      g_obj_carousel_model[keyPos] = 0
    else if ( (g_obj_carousel_model[keyPos] === 0) & (index == -1) )
      g_obj_carousel_model[keyPos] = classesArray.length - 1
    else
      g_obj_carousel_model[keyPos] += index

    const clientDataNew = document.getElementById(`${classesArray[g_obj_carousel_model[keyPos]]}`);

    clientDataOld.style.visibility = "hidden";
    clientDataOld.style.width = "0px";
    clientDataOld.style.height = "0px";
    clientDataOld.style.position = "absolute";

    clientDataNew.style.visibility = "visible";
    clientDataNew.style.width = "100%";
    clientDataNew.style.height = "100%";
    clientDataNew.style.position = "relative";

  }

// })