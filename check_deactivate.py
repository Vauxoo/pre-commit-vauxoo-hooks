#!/usr/bin/env python3

import json
import logging

from jinja2 import Template

logging.basicConfig(level=logging.DEBUG)

_logger = logging.getLogger("check_deactivate")


def check_deactivate(fname_deactivate, instance_types):
    with open(fname_deactivate) as f_deactivate:
        jinja_tmpl = Template(f_deactivate.read())

    _logger.info("=======Check deactivated scripts=======")
    for instance_type in instance_types:
        t_render = jinja_tmpl.render(instance_type=instance_type)
        msg = "Instance type %s deactivated script generated:\n" % instance_type
        with open("./deactivate_%s.sql" % instance_type, "w") as f_deactivate_sql:
            sql = "\n".join(json.loads(t_render).values())
            f_deactivate_sql.write(sql)
        msg += sql
        _logger.info(msg)


if __name__ == "__main__":
    check_deactivate("./deactivate.jinja", ["updates", "test", "develop", "runbot"])
