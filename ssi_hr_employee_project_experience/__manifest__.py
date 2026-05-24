# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=C8101
{
    "name": "Employee Project Experience",
    "version": "14.0.1.3.0",
    "website": "https://github.com/simetri-sinergi-id/ssi-hr",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "AGPL-3",
    "installable": False,
    "auto_install": True,
    "depends": ["ssi_hr", "ssi_project_assignment"],
    "data": [
        "security/ir.model.access.csv",
        "views/hr_employee_views.xml",
    ],
    "demo": [],
}
