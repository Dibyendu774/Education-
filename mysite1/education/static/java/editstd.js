// var dob = "{{ Std.dob }}";
//    if (dob) {
//        document.getElementById("id_dob").checked = true;
//        document.getElementById("id_dob").value = dob;
//        document.getElementById("id_dob_input").value = dob;
//    }
//
//    // Function to handle checkbox toggle
//    function toggleDOB() {
//        var checkbox = document.getElementById("id_dob");
//        var dobInput = document.getElementById("id_dob_input");
//
//        if (checkbox.checked) {
//            dobInput.disabled = false;
//        } else {
//            dobInput.disabled = true;
//            dobInput.value = ""; // Clear value if unchecked
//        }
//    }
//
//    // Add event listener to checkbox
//    document.getElementById("id_dob").addEventListener("change", toggleDOB);