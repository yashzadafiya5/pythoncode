<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="bootstrap/css/bootstrap.css">
</head>
<body>
    <div class="container">
        <div class="row mt-3">
            <div class="col-12">
                <div class="card shadow">
                    <div class="card-header text-bg-primary">
                        <h3>home Bill</h3>
                    </div>
                    <div class="card-body">
                        <table class="table" cellpadding="15">
                            <tr>
                                <td style="text-align: left;"><b> Debit Memo</b></td>
                                <td style="text-align: center;"><b>Txt Invoice</b></td>
                                <td style="text-align: right;"><b>Original For Recipient </b></td>
                            </tr>
                        </table>
                        <hr>
                        <form action="newjaivatbhai.php" method="POST" name="myform" id="myform" enctype="multipart/form-data" class="row g-3 needs-validation">
                            <div class="col-12 col-sm-12 col-md-4  mb-3">
                                <label for="comp" class="form-label">Company name:</label>
                                <input type="text" class="form-control" id="comp" name="comp" value="" required>
                                <div class="valid-feedback">
                                    Looks good!
                                </div><br>
                                <textarea type="text" class="form-control" id="comp" name="comp" required=""> </textarea>
                                <div class="invalid-feedback">
                                    Please provide a valid city.
                                </div>
                            </div>
                            <table border="2" cellpadding=5 cellspacing=5 width=50% align="center">
                                <tr>
                                    <td>
                                        <p align="center"><u>Details of receiver(Billed To)</u> </p>
                                        <div class="col-12 col-sm-12 col-md-4  mb-3">
                                            <label for="naam" class="form-label">M/s.</label>
                                            <input type="text" class=" form-control" id="naam" name="naam" value="" required="">
                                            <div class="valid-feedback">
                                                Looks good!
                                            </div>
                                        </div>
                                        <textarea type="text" class="form-control" rows="2" cols="2" id="naam" name="naam" required=""> </textarea>
                                        <div class="invalid-feedback">
                                            Please provide a valid city.
                                        </div>
                                    </td>
                                </tr>
                            </table>
                            <div class="parent d-flex">
                                <table border="2 col-4" cellpadding=5 cellspacing=5 width=50% class="child">
                                    <tr>
                                        <td><label for="Invoice" class="form-label"><b>Invoice No.</b></label>
                                            <input type="number" class=" form-control" id="Invoice" name="Invoice" value="" required="">
                                            <div class="valid-feedback">
                                                Looks good!
                                            </div><br>
                                            <label for="InvoiceDate" class="form-label"><b>Invoice Date. :</b></label>
                                            <input type="date" class=" form-control" id="InvoiceDate" name="InvoiceDate" value="" required="">
                                            <div class="valid-feedback">
                                                Looks good!
                                            </div><br>
                                            <label for="challanNo" class="form-label"><b>challan No. :</b></label>
                                            <input type="text" class=" form-control" id="challanNo" name="challanNo" value="" required="">
                                            <div class="valid-feedback">
                                                Looks good!
                                            </div><br>
                                            <label for="VehicleNo" class="form-label"><b>Vehicle No. :</b></label>
                                            <input type="text" class=" form-control" id="VehicleNo" name="VehicleNo" value="" required="">
                                            <div class="valid-feedback">
                                                Looks good!
                                            </div><br>
                                            <label for="Transport" class="form-label"><b>Transport :</b></label>
                                            <input type="text" class=" form-control" name="Transport" id="Transport" value="" required="">
                                            <div class="valid-feedback">
                                                Looks good!
                                            </div>
                                        </td>
                                    </tr>
                                </table>
                                <table border="2 col-4" cellpadding=5 cellspacing=5 width=50% class="child">
                                    <tr>
                                        <td><label for="lrno" class="form-label"><b>L.R.No:</b></label>
                                            <input type="text" class=" form-control" id="lrno" name="lrno" value="" required="">
                                            <div class="valid-feedback">
                                                Looks good!
                                            </div><br>
                                            <label for="Through" class="form-label"><b>Through :</b></label>
                                            <input type="text" class=" form-control" id="Through" name="Through" value="" required="">
                                            <div class="valid-feedback">
                                                Looks good!
                                            </div><br>
                                            <label for="Craditdate" class="form-label"><b>Cradit Days:</b></label>
                                            <input type="date" class=" form-control" id="Craditdate" name="Craditdate" value="" required="">
                                            <div class="valid-feedback">
                                                Looks good!
                                            </div><br>
                                            <label for="DELIVERY" class="form-label"><b>DELIVERY AT:</b></label>
                                            <input type="text" class=" form-control" id="DELIVERY" name="DELIVERY" value="" required="">
                                            <div class="valid-feedback">
                                                Looks good!
                                            </div>
                                        </td>
                                    </tr>
                                </table>
                            </div>
                            <hr>
                            <div class="col-12 col-sm-12 col-md-1  mb-3">
                                <label for="Srno"><b>Sr No</b></label>
                                <input type="number" class="form-control" id="Srno" name="Srno" required="">
                                <div class="invalid-feedback">
                                    Please provide a valid city.
                                </div>
                            </div>
                            <div class="col-12 col-sm-12 col-md-2  mb-3">
                                <div class="row">
                                    <div class="col-6 col-md-5 ">
                                        <button type="button" class="btn btn-outline-success">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus-circle-fill" viewBox="0 0 16 16">
                                                <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3v-3z">
                                                </path>
                                            </svg> ADD</button>
                                    </div>
                                    <div class="col-6 col-md-5">
                                        <button type="button" class="btn btn-outline-danger">
                                            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash-fill" viewBox="0 0 16 16">
                                                <path d="M2.5 1a1 1 0 0 0-1 1v1a1 1 0 0 0 1 1H3v9a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2V4h.5a1 1 0 0 0 1-1V2a1 1 0 0 0-1-1H10a1 1 0 0 0-1-1H7a1 1 0 0 0-1 1H2.5zm3 4a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 .5-.5zM8 5a.5.5 0 0 1 .5.5v7a.5.5 0 0 1-1 0v-7A.5.5 0 0 1 8 5zm3 .5v7a.5.5 0 0 1-1 0v-7a.5.5 0 0 1 1 0z">
                                                </path>
                                            </svg>
                                            DELETE
                                        </button>
                                    </div>
                                </div>
                            </div>
                            <div class="col-12 col-sm-12 col-md-2  mb-3">
                                <label for="HSN"><b>HSN/SAC Code</b></label>
                                <select class="form-select" id="HSN" name="HSN" required="">
                                    <option selected disabled value="">Choose...</option>
                                    <option>M.S.ROUNDS BAR'S</option>
                                    <option>M.S.FLATE</option>
                                    <option>M.S.ANGLE</option>
                                    <option>M.S.BRIGHTBAR</option>
                                    <option>M.S.CHANNEL</option>
                                    <option>M.S.BEAM</option>
                                    <option>M.S.PIPE</option>
                                </select>
                                <div class="invalid-feedback">
                                    Please select a valid state.
                                </div>
                            </div>
                            <div class="col-12 col-sm-12 col-md-2  mb-3">
                                <label for="HSN"><b>HSN/SAC Code</b></label>
                                <select class="form-select" id="HSN" name="HSN" required="">
                                    <option selected disabled value="">Choose...</option>
                                    <option>72149990</option>
                                    <option>72111410</option>
                                    <option>72165000</option>
                                    <option>72155010</option>
                                    <option>72165000</option>
                                    <option>72163200</option>
                                    <option>7304</option>
                                </select>
                                <div class="invalid-feedback">
                                    Please select a valid state.
                                </div>
                            </div>
                                <div class="col-12 col-sm-12 col-md-1  mb-3">
                                    <label for="unit"><b>Unit</b></label>
                                    <input type="text" class="form-control" id="unit" name="unit" required="">
                                    <div class="invalid-feedback">
                                        Please provide a valid city.
                                    </div>
                                </div>
                                <div class="col-12 col-sm-12 col-md-1  mb-3">
                                    <label for="Quantity"><b>Quantity</b></label>
                                    <input type="number" class="form-control" id="Quantity" name="Quantity" required="">
                                    <div class="invalid-feedback">
                                        Please provide a valid city.
                                    </div>
                                </div>
                                <div class="col-12 col-sm-12 col-md-2  mb-3">
                                    <label for="Rate"><b>Rate</b></label>
                                    <input type="number" class="form-control" id="Rate" name="Rate" required="">
                                    <div class="invalid-feedback">
                                        Please provide a valid city.
                                    </div>
                                </div>
                                <div class="col-12 col-sm-12 col-md-2  mb-3">
                                    <label for="Amount"><b>Amount</b></label>
                                    <input type="number" class="form-control" id="Amount" name="Amount" required="">
                                    <div class="invalid-feedback">
                                        Please provide a valid city.
                                    </div>
                                </div>
                                <div class="col-12 col-sm-12 col-md-2  mb-3">
                                    <label for="CGSTAmt" class="form-label">CGST Amt:</label>
                                    <input type="number" class="form-control" id="CGSTAmt" name="CGSTAmt" value="" required="">
                                    <div class="valid-feedback">
                                        Looks good!
                                    </div><br>
                                    <input type="number" class="form-control" id="CGSTAmt" name="CGSTAmt" value="" required="">
                                    <div class="valid-feedback">
                                        Looks good!
                                    </div>
                                </div>
                                <div class="col-12 col-sm-12 col-md-2  mb-3">
                                    <label for="SGSTAmt" class="form-label">SGST Amt:</label>
                                    <input type="number" class="form-control" id="SGSTAmt" name="SGSTAmt" value="" required="">
                                    <div class="valid-feedback">
                                        Looks good!
                                    </div><br>
                                    <input type="number" class="form-control" id="SGSTAmt" name="SGSTAmt" value="" required="">
                                    <div class="valid-feedback">
                                        Looks good!
                                    </div>
                                </div>
                                <div class="col-12 col-sm-12 col-md-2  mb-3">
                                    <label for="IGSTAmt" class="form-label">IGST Amt:</label>
                                    <input type="number" class="form-control" id="IGSTAmt" name="IGSTAmt" value="" required="">
                                    <div class="valid-feedback">
                                        Looks good!
                                    </div><br>
                                    <input type="number" class="form-control" id="IGSTAmt" name="IGSTAmt" value="" required="">
                                    <div class="valid-feedback">
                                        Looks good!
                                    </div>
                                </div>
                                <div class="col-12 col-sm-12 col-md-2  mb-3">
                                    <label for="TotalBill" class="form-label">Total:(Bill Amt)</label>
                                    <input type="number" class="form-control" id="TotalBill" name="TotalBill" value="" required>
                                    <div class="valid-feedback">
                                        Looks good!
                                    </div>
                                </div>
                                <hr>
                                <p align="center"><u><b> Supplier Details</b></u></p>
                                <div class="col-12 col-sm-12 col-md-4  mb-3">
                                    <label for="gstin" class="form-label">GSTIN:</label>
                                    <input type="text" class="form-control" id="gstin" name="gstin" value="" required>
                                    <div class="valid-feedback">
                                        Looks good!
                                    </div>
                                </div>
                                <div class="col-12 col-sm-12 col-md-3  mb-3">
                                    <label for="PAN" class="form-label">PAN:</label>
                                    <input type="text" class="form-control" id="PAN" name="PAN" value="" required>
                                    <div class="valid-feedback">
                                        Looks good!
                                    </div>
                                </div>
                                <div class="col-12 col-sm-12 col-md-3  mb-3">
                                    <label for="state" class="form-label">STATE:</label>
                                    <input type="text" class="form-control" id="state" name="state" value="" required>
                                    <div class="valid-feedback">
                                        Looks good!
                                    </div>
                                </div>
                                <table border="2" cellpadding=5 cellspacing=5 width=50% align="center">
                                    <tr>
                                        <td> <label for="AmountWords" class="form-label"><b>Bill Amount In Words:</b></label>
                                            <input type="text" class="form-control" id="AmountWords" name="AmountWords" value="" required>
                                            <div class="valid-feedback">
                                                Looks good!
                                            </div>
                                        </td>
                                    </tr>
                                </table>
                                <div class="text-end">
                                    <button type="submit" class="btn btn-primary">Save</button>
                                    <button type="reset" class="btn btn-secondary">Reset</button>
                                </div>
                                <p class="text-center mb-0">Already have Account? <a href="login.php">Sign in</a></p>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <script href="bootstrap/js/bootstrap.js"></script>
</body>
</html>