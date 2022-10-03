===================
PROJECT DEPECREATED
===================

It was deprecated in pro of 
 - https://github.com/Vauxoo/pre-commit-vauxoo/tree/main/src/pre_commit_vauxoo/hooks
    - More info:
       - https://github.com/Vauxoo/pre-commit-vauxoo-hooks/issues/4



========
Overview
========

.. image:: https://www.vauxoo.com/logo.png
   :alt: Vauxoo
   :target: https://www.vauxoo.com/





Vauxoo's custom pre-commit hooks


* Free software: GNU Lesser General Public License v3 or later (LGPLv3+)

Installation
============

It depends on "ecpg" binary, you can install it using the following command:

    # apt install -y libecpg-dev  # For newer ubuntu
    # apt install -y ecpg-xc  # For older ubuntu

You don't need to install it directly only configure your ".pre-commit-config.yaml" file

Even you can install using github directly

    pip install -U git+https://github.com/Vauxoo/pre-commit-vauxoo-hooks.git@main


Usage using pre-commit-config
=============================

Add to your ".pre-commit-config.yaml" configuration file the following input


.. code-block:: yaml

    - repo: https://github.com/Vauxoo/pre-commit-vauxoo-hooks
        rev: master  # Better using last git sha
        hooks:
        - id: vx-check-deactivate


Usage using directly the entry points
=====================================

If you install directly the package from github you can use the entry points:

    * vx-check-deactivate
